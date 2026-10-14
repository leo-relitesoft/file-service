import asyncio
from aiobotocore.session import get_session

class AsyncS3Client:
    def __init__(self, access_key, secret_key, endpoint_url, bucket_name):
        self.config = {
            "aws_access_key_id": access_key,
            "aws_secret_access_key": secret_key,
            "endpoint_url": endpoint_url,
        }
        self.bucket_name = bucket_name
        self.session = get_session()

    async def upload_file(self, local_path, s3_key):
        # Контекстный менеджер создает клиент под каждую сессию
        async with self.session.create_client('s3', **self.config) as client:
            with open(local_path, 'rb') as f:
                await client.put_object(Bucket=self.bucket_name, Key=s3_key, Body=f)
            print(f"Файл {s3_key} загружен асинхронно.")

    async def download_file(self, s3_key, local_path):
        async with self.session.create_client('s3', **self.config) as client:
            response = await client.get_object(Bucket=self.bucket_name, Key=s3_key)
            async with response['Body'] as stream:
                data = await stream.read()
                with open(local_path, 'wb') as f:
                    f.write(data)
            print(f"Файл {s3_key} скачан асинхронно.")

# Пример запуска асинхронного кода:
async def main():
    s3 = AsyncS3Client(
        access_key='ВАШ_ACCESS_KEY',
        secret_key='ВАШ_SECRET_KEY',
        endpoint_url='https://your-provider.com',
        bucket_name='my-cool-bucket'
    )
    await s3.upload_file('test.txt', 'remote_test.txt')

if __name__ == '__main__':
    asyncio.run(main())
