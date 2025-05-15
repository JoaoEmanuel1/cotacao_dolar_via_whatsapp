import requests #Realiza requisições HTTP (Receber dados via API)
import pywhatkit as wk #Envia mensagens no WhatsApp
import time #Pausas no código

def pegar_cotacao_dolar():
    try:
        #Realiza a requisição HTTP a fim de receber os dados via API
        url = "https://economia.awesomeapi.com.br/last/USD-BRL"
        response = requests.get(url)

        #Verifica se a requisição funcionou corretamente
        response.raise_for_status()
        data = response.json()

        #Pega a cotação atual do dólar
        cotacao_dolar = float(data["USDBRL"]["bid"])
        return (
            "📢 *Bot de Cotação do Dólar*\n"
            "━━━━━━━━━━━━━━━━━━━━━━━\n"
            "💰 *Cotação atual do Dólar:*\n"
            f"➡️ R$ {cotacao_dolar:.2f}\n"
            "━━━━━━━━━━━━━━━━━━━━━━━\n"
            "⏰ *Atualização diária às 9h*\n"
            "✅ Fique ligado para não perder!\n\n"
            "🤖 *Obrigado por usar o nosso bot!*"
        )

    
    except Exception as e:
        print(f"Erro ao pegar cotação: {e}")
        return None

def enviar_mensagem_whatsapp():
    #Recebe a mensagem da cotação atual
    message = pegar_cotacao_dolar()
    if not message:
        print("Não foi possível obter a cotação.")
        return

    try:
        #Faz o envio da mensagem via WhatsApp
        wk.sendwhatmsg_instantly(
            phone_no="+5538999999999", #substitua pelo seu numero para usar
            message=message,
            wait_time=20,
            tab_close=True
        )
        print("Mensagem enviada com sucesso!")

    except Exception as e:
        print(f"Erro ao enviar mensagem: {e}")

#Início Execução
if __name__ == "__main__":
    print("Bot Cotação Dólar Iniciado...")
    enviar_mensagem_whatsapp()