# ============================
# INFORMACIÓN GENERAL DE LA TIENDA
# ============================

STORE_INFO = {
    "envios": "Realizamos envíos a todo el país mediante OCA y Andreani. Tiempo estimado: 3 a 7 días hábiles.",
    "devoluciones": "Aceptamos cambios y devoluciones dentro de los 15 días con ticket o comprobante.",
    "horarios": "Lunes a Sábado de 10:00 a 19:00.",
    "sucursales": [
        "Av. Rivadavia 4500, CABA",
        "Av. San Martín 1220, Córdoba",
        "Av. Pellegrini 900, Rosario"
    ]
}

# ============================
# PRODUCTOS - LA TRANQUERA
# ============================

PRODUCTS = [

    # ---------- PONCHOS ----------
    {
        "id": 1,
        "nombre": "Poncho Salteño Tejido a Mano",
        "categoria": "ponchos",
        "precio": 65000,
        "talles": ["Único"],
        "stock": 10,
        "imagen": "poncho1.jpg"
    },
    {
        "id": 2,
        "nombre": "Poncho Pampa Rayado Tradicional",
        "categoria": "ponchos",
        "precio": 72000,
        "talles": ["Único"],
        "stock": 8,
        "imagen": "poncho2.jpg"
    },
    {
        "id": 3,
        "nombre": "Poncho Criollo Artesanal",
        "categoria": "ponchos",
        "precio": 78000,
        "talles": ["Único"],
        "stock": 6,
        "imagen": "poncho3.jpg"
    },

    # ---------- BOMBACHAS ----------
    {
        "id": 4,
        "nombre": "Bombacha de Campo Clásica",
        "categoria": "bombachas",
        "precio": 28000,
        "talles": ["S", "M", "L", "XL", "XXL"],
        "stock": 30,
        "imagen": "bombacha1.jpg"
    },
    {
        "id": 5,
        "nombre": "Bombacha Entallada Premium",
        "categoria": "bombachas",
        "precio": 33000,
        "talles": ["S", "M", "L", "XL"],
        "stock": 22,
        "imagen": "bombacha2.jpg"
    },
    {
        "id": 6,
        "nombre": "Bombacha Pampa de Trabajo",
        "categoria": "bombachas",
        "precio": 31000,
        "talles": ["M", "L", "XL"],
        "stock": 18,
        "imagen": "bombacha3.jpg"
    },

    # ---------- ALPARGATAS ----------
    {
        "id": 7,
        "nombre": "Alpargatas de Yute Tradicionales",
        "categoria": "alpargatas",
        "precio": 15000,
        "talles": ["38", "39", "40", "41", "42", "43", "44"],
        "stock": 40,
        "imagen": "alpargatas1.jpg"
    },
    {
        "id": 8,
        "nombre": "Alpargatas de Lona Negra",
        "categoria": "alpargatas",
        "precio": 16500,
        "talles": ["38", "39", "40", "41", "42", "43"],
        "stock": 35,
        "imagen": "alpargatas2.jpg"
    },
    {
        "id": 9,
        "nombre": "Alpargatas de Lona Cruda",
        "categoria": "alpargatas",
        "precio": 16000,
        "talles": ["39", "40", "41", "42", "43"],
        "stock": 28,
        "imagen": "alpargatas3.jpg"
    },

    # ---------- FAJAS ----------
    {
        "id": 10,
        "nombre": "Faja Tejida Tradicional",
        "categoria": "fajas",
        "precio": 18000,
        "talles": ["Único"],
        "stock": 20,
        "imagen": "faja1.jpg"
    },
    {
        "id": 11,
        "nombre": "Faja Pampa Bordada",
        "categoria": "fajas",
        "precio": 21000,
        "talles": ["Único"],
        "stock": 15,
        "imagen": "faja2.jpg"
    },
    {
        "id": 12,
        "nombre": "Faja Gaucha Tejida a Mano",
        "categoria": "fajas",
        "precio": 23000,
        "talles": ["Único"],
        "stock": 12,
        "imagen": "faja3.jpg"
    },

    # ---------- SOMBREROS ----------
    {
        "id": 13,
        "nombre": "Sombrero Criollo de Ala Ancha",
        "categoria": "sombreros",
        "precio": 68000,
        "talles": ["S", "M", "L"],
        "stock": 10,
        "imagen": "sombreros1.jpg"
    },
    {
        "id": 14,
        "nombre": "Sombrero Pampeano de Fieltro",
        "categoria": "sombreros",
        "precio": 72000,
        "talles": ["M", "L"],
        "stock": 8,
        "imagen": "sombreros2.jpg"
    },
    {
        "id": 15,
        "nombre": "Sombrero de Campo Artesanal",
        "categoria": "sombreros",
        "precio": 85000,
        "talles": ["Único"],
        "stock": 6,
        "imagen": "sombreros3.jpg"
    },

    # ---------- CAMISAS ----------
    {
        "id": 16,
        "nombre": "Camisa Gaucha rayada",
        "categoria": "camisas",
        "precio": 24000,
        "talles": ["S", "M", "L", "XL"],
        "stock": 30,
        "imagen": "camisa1.jpg"
    },
    {
        "id": 17,
        "nombre": "Camisa de Lino azul",
        "categoria": "camisas",
        "precio": 31000,
        "talles": ["M", "L", "XL"],
        "stock": 20,
        "imagen": "camisa2.jpg"
    },
        {
        "id": 33,
        "nombre": "Camisa de Lino verde",
        "categoria": "camisas",
        "precio": 31000,
        "talles": ["M", "L", "XL"],
        "stock": 20,
        "imagen": "camisa3.jpg"
    },

    # ---------- CHALECOS ----------
    {
        "id": 18,
        "nombre": "Chaleco de Cuero Marrón",
        "categoria": "chalecos",
        "precio": 75000,
        "talles": ["M", "L", "XL"],
        "stock": 12,
        "imagen": "chaleco1.jpg"
    },
    {
        "id": 19,
        "nombre": "Chaleco Tejido Artesanal",
        "categoria": "chalecos",
        "precio": 42000,
        "talles": ["S", "M", "L"],
        "stock": 18,
        "imagen": "chaleco2.jpg"
    },

    # ---------- CINTOS ----------
    {
        "id": 20,
        "nombre": "Cinto Trenzado de Cuero",
        "categoria": "cintos",
        "precio": 22000,
        "talles": ["90", "95", "100", "105", "110"],
        "stock": 25,
        "imagen": "cintos1.jpg"
    },
    {
        "id": 21,
        "nombre": "Cinto Pampa Bordado",
        "categoria": "cintos",
        "precio": 26000,
        "talles": ["95", "100", "105"],
        "stock": 18,
        "imagen": "cintos2.jpg"
    },
    {
        "id": 22,
        "nombre": "Cinto Gaucho Artesanal",
        "categoria": "cintos",
        "precio": 28000,
        "talles": ["100", "105", "110"],
        "stock": 14,
        "imagen": "cintos3.jpg"
    },

    # ---------- BOINAS ----------
    {
        "id": 23,
        "nombre": "Boina Vasca Negra",
        "categoria": "boinas",
        "precio": 12000,
        "talles": ["S", "M", "L"],
        "stock": 22,
        "imagen": "boina1.jpg"
    },
    {
        "id": 24,
        "nombre": "Boina de Lana Gris",
        "categoria": "boinas",
        "precio": 13500,
        "talles": ["M", "L"],
        "stock": 16,
        "imagen": "boina2.jpg"
    },

    # ---------- MATES ----------
    {
        "id": 25,
        "nombre": "Mate Camionero de Cuero",
        "categoria": "mates",
        "precio": 18000,
        "talles": ["Único"],
        "stock": 20,
        "imagen": "mate1.jpg"
    },
    {
        "id": 26,
        "nombre": "Mate Imperial Grabado",
        "categoria": "mates",
        "precio": 26000,
        "talles": ["Único"],
        "stock": 12,
        "imagen": "mate2.jpg"
    },
    {
        "id": 27,
        "nombre": "Mate Torpedo Artesanal",
        "categoria": "mates",
        "precio": 23000,
        "talles": ["Único"],
        "stock": 15,
        "imagen": "mate3.jpg"
    },

    # ---------- MATERAS ----------
    {
        "id": 28,
        "nombre": "Matera de Cuero Repujado",
        "categoria": "materas",
        "precio": 32000,
        "talles": ["Único"],
        "stock": 10,
        "imagen": "matera1.jpg"
    },
    {
        "id": 29,
        "nombre": "Matera de Lona con Cuero",
        "categoria": "materas",
        "precio": 27000,
        "talles": ["Único"],
        "stock": 14,
        "imagen": "matera2.jpg"
    },

    # ---------- CUCHILLOS ----------
    {
        "id": 30,
        "nombre": "Cuchillo Criollo Hoja de Acero",
        "categoria": "cuchillos",
        "precio": 38000,
        "talles": ["Único"],
        "stock": 8,
        "imagen": "cuchillo1.jpg"
    },
    {
        "id": 31,
        "nombre": "Facón con Vaina de Cuero",
        "categoria": "cuchillos",
        "precio": 52000,
        "talles": ["Único"],
        "stock": 6,
        "imagen": "cuchillo2.jpg"
    },
    {
        "id": 32,
        "nombre": "Cuchillo Artesanal Forjado",
        "categoria": "cuchillos",
        "precio": 68000,
        "talles": ["Único"],
        "stock": 5,
        "imagen": "cuchillo3.jpg"
    },
]