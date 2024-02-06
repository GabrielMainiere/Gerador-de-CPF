# Gerador de CPF

Este é um gerador de números de CPF em Python.

## Funcionamento

- O programa gera números de CPF válidos de forma aleatória seguindo as regras de validação de CPF do Brasil. O CPF é composto por 11 dígitos, sendo os dois últimos dígitos os dígitos verificadores, que são calculados com base nos primeiros 9 dígitos.

Para gerar um CPF, o programa realiza os seguintes passos:

1. Gera aleatoriamente 9 dígitos.
2. Calcula o primeiro dígito verificador usando um algoritmo específico.
3. Calcula o segundo dígito verificador com base nos 9 dígitos anteriores e no primeiro dígito verificador.
4. Combina os dígitos gerados para formar um número de CPF válido.

O programa então imprime o CPF gerado na saída padrão.

## Exemplo de Saída
- CPF gerado: 123.456.789-09

## Contribuição

- Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request se encontrar algum problema ou tiver uma sugestão de melhoria.

## Licença

- Este projeto é licenciado sob a Licença MIT. Consulte o arquivo [LICENSE](LICENSE) para obter mais detalhes.
