# 🐍 Hola Mundo — Python en Cloudflare Pages desde GitHub

## Estructura del repo

```
tu-repo/
├── index.html              ← Página principal
├── wrangler.toml           ← Config de Cloudflare
└── functions/
    └── api/
        └── hello.py        ← Tu función Python en el edge
```

---

## Pasos para desplegar

### 1. Sube a GitHub
```bash
git init
git add .
git commit -m "Hola Mundo Python"
git remote add origin https://github.com/tu-usuario/tu-repo.git
git push -u origin main
```

### 2. Conecta Cloudflare Pages
1. Ve a [dash.cloudflare.com](https://dash.cloudflare.com) → **Pages**
2. Click **Create a project** → **Connect to Git**
3. Selecciona tu repositorio de GitHub
4. En la configuración de build:
   - **Framework preset**: None
   - **Build command**: *(dejar vacío)*
   - **Build output directory**: `.`  (un punto)
5. Click **Save and Deploy**

### 3. ¡Listo! 🎉
- Tu sitio estará en: `https://hola-mundo-python.pages.dev`
- La API Python en: `https://hola-mundo-python.pages.dev/api/hello`

---

## Cómo funciona

Cloudflare Pages Functions permite correr Python directamente en el **edge** (sin servidor).  
El archivo `functions/api/hello.py` se convierte automáticamente en la ruta `/api/hello`.

---

## Actualizaciones automáticas
Cada `git push` a `main` redespliega el sitio automáticamente. Sin CI/CD extra.
