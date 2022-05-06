def format_headers(headers_str: str, no_colon: bool = True) -> dict:
    """格式化浏览器请求值为dict

    Args:
        headers_str (str): 浏览器中直接复制出来的请求值
        no_colon (bool, optional): 请求值中是否包含:开头的参数（请求信息）. Defaults to True.

    Returns:
        dict
    """
    data = {}
    headers_list = headers_str.split("\n")
    for header in headers_list:
        header = header.lstrip()
        if header == "":
            continue
        if header.startswith(":"):
            if no_colon:
                continue
            split_index = header[1:].index(":") + 1
        else:
            split_index = header.index(":")
        data[header[:split_index]] = header[split_index + 1 :].lstrip()
    return data
