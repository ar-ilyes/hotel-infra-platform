resource "google_container_cluster" "primary" {
  name     = "hotel-platform-europe"
  location = "europe-west1"
  
  node_config {
    machine_type = "e2-standard-4"
    disk_size_gb = 100
  }
  
  autoscaling {
    min_node_count = 3
    max_node_count = 10
  }
}
