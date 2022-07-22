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

resource "aws_s3_bucket" "de-bucket" {
  bucket = "de-s3-bucket-v01"
  tags = {
    "name" = "de-s3"
  }
}

resource "aws_s3_bucket_acl" "de-acl" {
  bucket = aws_s3_bucket.de-bucket.id
  acl = "private"
}

resource "aws_redshift_cluster" "de-redshift" {
  cluster_identifier = "de-redshift-v01"
  database_name = var.database_credential
  master_password = var.database_credential
  
}