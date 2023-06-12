resource "docker_image" "this" {
  name         = "nginx"
  keep_locally = false
}

resource "docker_container" "this" {
  image = docker_image.this.image_id
  name  = var.container_name
  ports {
    internal = 80
    external = 8000
  }
}
