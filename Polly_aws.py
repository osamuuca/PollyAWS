import boto3

pol = boto3.Session(
                aws_access_key_id='ASIA4RPOQIBYENU4AHXK',
                aws_secret_access_key='uUPAPs69SDs1b0UAEi16Z1MG2CegSKMmAzgi5lbH',
                aws_session_token='FwoGZXIvYXdzEJL//////////wEaDENRlkDzIejjc/toXiLSAR7x/L5G/gmPCM2m4WuaXWJ4djgElpltv5RAMX+jVcoOUDm0wn98L1tWEal5YIUyRWUTnmDciRA+5xvZ74ACoXFT+ysVy0ceT2H/n+Jku5eGipPyrfxj/nu7B7mdDJJ0mVnfqbXCK36ToNBT7DT4EZsKTRMQbzTOwhWYIqpW+H1MLgrJq8++O/8Lxus+YukXevNgi0y4Cs4aEi8nhYrD0Pu1fnJWd5IQgaH64IpgDYziE34LvZ0RANT9rfBgPNPd3QUih/U+u3iz/sTay2AE2fG5CCj1ybCUBjItkhVQ5dZAhyXAAkbOrJNt0i749kGWiftjVIXu4d2YJqw+V0ykwjNS/lmMWKeZ',
                region_name='us-east-1').client('polly')


def text_to_voice(text, name):
    response = pol.synthesize_speech(Text=text, VoiceId='Camila', OutputFormat='mp3')
    body = response['AudioStream'].read()

    file_name = f'{name}.mp3'

    with open(file_name, 'wb') as file:
        file.write(body)
        file.close()


if __name__ == '__main__':
    text_to_voice(text=input('Insira o texto que será lido: '),
                  name=input('Insira o nome do arquivo desejado: '))
