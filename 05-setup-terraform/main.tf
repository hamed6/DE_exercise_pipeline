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
  cluster_identifier = var.cluster_id
  database_name = "ny_taxi"
  master_username = var.database_credential_user
  master_password = var.database_credential_pass
  node_type = var.node_type
  cluster_type = var.cluster_type
}