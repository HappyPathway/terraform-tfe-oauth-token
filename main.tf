data "external" "module_publish" {
  program = ["python", "${path.module}/scripts/oauth_tokens.py"]

  query = {
    tfe_org       = "${var.tfe_org}"
    tfe_api = "${var.tfe_api}"
    tfe_token = "${var.tfe_token}"
  }
}


output "oauth_token" {
  value = "${data.external.module_publish.result["oauth_token"]}"
}