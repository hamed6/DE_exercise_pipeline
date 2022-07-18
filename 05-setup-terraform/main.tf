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

resource "aws_vpc" "vpc_from_terraform" {
    name="my-vpc-02"
    cidr_block="10.0.0.0/28"  
}