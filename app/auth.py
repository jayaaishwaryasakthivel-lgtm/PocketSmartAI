
def current_user(request: Request):
    auth_header = request.headers.get("Authorization", "")
    token = request.cookies.get("access_token")

    if not token and auth_header.lower().startswith("bearer "):
        token = auth_header[7:].strip()

    if not token:
        raise HTTPException(
            status_code=401,
            detail="Authentication required. Please log in again."
        )

    user_id = decode_token(token)
    user = get_user_by_id(user_id)

    if not user:
        raise HTTPException(
            status_code=401,
            detail="User session expired. Please log in or register again."
        )

    return user
