terraform {
    required_providers{
        aws={
            source="hashicorp/aws"
            version="~> 3.0"
        }
    }
}

provider "aws" {
  region = "us-east-1"
}

resource "aws_internet_gateway" "gw" {
    vpc_id = "vpc-0a89240b868bfa1db"
    
    tags = {
      "name" = "macrack-igw-01"
    }
}