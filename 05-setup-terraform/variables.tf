variable "cluster_id" {
  default = "de-redshift-v01"
}

variable "node_type" {
  default = "dc2.large"
}

variable "cluster_type" {
  default = "single-node"
}
variable "database_credential_user" {
    default  = "root"    
}

variable "database_credential_pass" {
    description = "enter default value"
}