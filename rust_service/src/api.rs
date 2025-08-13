use axum::{routing::get, Router};

pub fn router() -> Router {
    Router::new().route("/health", get(|| async { "ok" }))
}

pub async fn run() {
    let app = router();
    // In a full implementation this would start a server.
    let _ = app;
}
