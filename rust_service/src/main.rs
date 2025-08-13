use rust_service::api;

#[tokio::main]
async fn main() {
    api::run().await;
}
