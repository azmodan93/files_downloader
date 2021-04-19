def save_file(content, filename):
    """Save content downloaded from a link to your local disk

    Args:
        content (Stream): Content that you need to save on a file
        filename (String): Filename
    """
    open(filename, 'wb').write(content)
