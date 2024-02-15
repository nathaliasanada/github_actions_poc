provider "aws" {
  region = "us-east-1"
}

terraform {
  backend "s3" {
    bucket = "github-actions-teste-tfstate"
    key    = "terraform.state"
    region = "us-east-1"
  }
}