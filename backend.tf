terraform {
  backend "s3" {
    bucket      = "hard-to-heat-homes-s3"
    key         = "hard-to-heat-homes-2.0/terraform.tfstate"
    region      = "eu-north-1"
    dynamodb_table = "state-table"
    encrypt     = true
  }
}