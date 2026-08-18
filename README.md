# Env Leak (`env-leak`)

**Category:** general · **Difficulty:** easy · **Points:** 175

The key sits in the process environment; read it from /proc or the container env.

## Run it

```bash
docker build -t sparflag/env-leak .
# `deca-ai start env-leak` (or the web UI) prints the docker run line with your
# SPARFLAG_SERVER + SPARFLAG_INSTANCE_TOKEN
```

## Recover the flag

The delivery blob is XOR-encrypted then base64-encoded. Discover the challenge key, then invert XOR+base64.

The plaintext flag is never written to disk or served — only the encoded delivery blob
is. When you have it:

```bash
deca-ai submit env-leak 'sparflag{...}'
```

## Hints

- Inspect environment variables inside the running container.
- Use that key to invert XOR+base64.
