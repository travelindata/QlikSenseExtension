import qvdrs

def read_qvd(file_path):
    """
    使用 qvdrs 读取 QVD 文件。
    
    Parameters:
        file_path (str): QVD 文件的路径。
        
    Returns:
        data (pd.DataFrame): 以 DataFrame 格式返回 QVD 文件的数据。
    """
    try:
        data = qvdrs.read(file_path)
        print(f"成功读取 QVD 文件: {file_path}")
        return data
    except Exception as e:
        print(f"读取 QVD 文件失败: {file_path}, 错误信息: {e}")
        return None

def write_qvd(data, file_path):
    """
    使用 qvdrs 将数据写入 QVD 文件。
    
    Parameters:
        data (pd.DataFrame): 要写入的 DataFrame 数据。
        file_path (str): QVD 文件的保存路径。
    """
    try:
        qvdrs.write(data, file_path)
        print(f"成功写入 QVD 文件: {file_path}")
    except Exception as e:
        print(f"写入 QVD 文件失败: {file_path}, 错误信息: {e}")