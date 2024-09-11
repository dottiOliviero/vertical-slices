def test_create_cat_success_return_cat(client, mocker):
    body = {"name": "a", "age": 12, "color": "green"}
    mocker.patch(
        "app.features.cat.create.handler.create_cat", return_value={"id": 1, **body}
    )
    response = client.post("/v1/cat/", json=body)
    assert response.status_code == 200
    assert response.json() == {"id": 1, **body}


def test_create_cat_error(client, mocker):
    body = {"name": "a", "age": 12, "color": "green"}
    mocker.patch("app.features.cat.create.handler.create_cat", return_value=None)
    response = client.post("/v1/cat/", json=body)
    assert response.status_code == 420
    assert response.json() == {"detail": "not able to create cat"}
