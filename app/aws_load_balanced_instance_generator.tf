provider "aws" {
  region = "<your_aws_region>"
}

locals {
  instance_type = "t2.micro"
}

resource "aws_security_group" "alb_sg" {
  name        = "alb-sg"
  description = "ALB Security Group"
  vpc_id      = "<your_vpc_id>"

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_security_group" "web_server_sg" {
  name        = "web-server-sg"
  description = "Web Server Security Group"
  vpc_id      = "<your_vpc_id>"

  ingress {
    from_port       = 80
    to_port         = 80
    protocol        = "tcp"
    security_groups = [aws_security_group.alb_sg.id]
  }
}

resource "aws_alb" "RENAME_ME" {
  name            = "RENAME_ME"
  internal        = false
  security_groups = [aws_security_group.alb_sg.id]
  subnets         = ["<your_subnet_id>"]
}

resource "aws_alb_listener" "RENAME_ME_alb_listener" {
  load_balancer_arn = aws_alb.RENAME_ME.arn
  port              = 80
  protocol          = "HTTP"

  default_action {
    type             = "forward"
    target_group_arn = aws_alb_target_group.RENAME_ME_alb_tg.arn
  }
}

resource "aws_alb_target_group" "RENAME_ME_alb_tg" {
  name     = "sbx-web-alb-tg"
  port     = 80
  protocol = "HTTP"
  vpc_id   = "<your_vpc_id>"
}

resource "aws_instance" "RENAME_ME" {
  ami                    = "ami-CHANGE_THIS_VALUE" # Amazon Linux 2 AMI, replace with the appropriate AMI ID for your region
  instance_type          = local.instance_type
  key_name               = "<your_key_pair_name>"
  vpc_security_group_ids = [aws_security_group.web_server_sg.id]

  user_data = <<-EOF
              #!/bin/bash
              sudo yum update -y
              sudo yum install -y httpd
              sudo systemctl start httpd
              sudo systemctl enable httpd
              echo "Hello, World!" > /var/www/html/index.html
              EOF

  tags = {
    Name = "RENAME_ME"
  }
}

resource "aws_alb_target_group_attachment" "RENAME_ME_alb_tg_attachment" {
  target_group_arn = aws_alb_target_group.RENAME_ME_alb_tg.arn
  target_id        = aws_instance.RENAME_ME_server.id
  port             = 80
}

output "alb_dns_name" {
  value = aws_alb.RENAME_ME_alb.dns_name
}
