# Guía de Preguntas Disponibles

Este documento lista todas las preguntas que puedes hacer al sistema de consulta de municipios de Oaxaca.

---

## 📋 Tipos de Consultas

### 1. Estado General del Municipio

Muestra todos los indicadores de carencia del municipio seleccionado.

**Formato:**
```
¿Cuál es el estado del municipio?
```

**Ejemplo de respuesta:**
```
📊 Estado de Abejones

Indicadores de Carencia:

🟠 Marginación: Alto
🟡 Rezago Social: Medio
🟢 Conectividad: Bajo
🟢 Servicios Básicos: Bajo
🟠 Elementos de Salud: Alto
🟠 Seguridad Social: Alto
🟠 Educación: Alto
🟡 Desigualdad: Medio
🟠 Dependencia Económica: Alto
🟡 Calidad de Vivienda: Medio
🟢 Seguridad Alimentaria: Bajo
```

---

### 2. Estado de un Indicador Específico

Consulta el nivel de carencia de un indicador particular.

**Formato:**
```
¿Cuál es el estado de [INDICADOR] del municipio?
```

**Indicadores disponibles:**
- `marginación` o `marginacion`
- `rezago social`
- `conectividad`
- `servicios básicos` o `servicios basicos`
- `elementos de salud`
- `seguridad social`
- `educación` o `educacion`
- `desigualdad`
- `dependencia económica` o `dependencia economica`
- `calidad de vivienda`
- `seguridad alimentaria`

**Ejemplos de preguntas:**
```
¿Cuál es el estado de educación del municipio?
¿Cuál es el estado de servicios básicos del municipio?
¿Cuál es el estado de marginación del municipio?
¿Cuál es el estado de rezago social del municipio?
¿Cuál es el estado de conectividad del municipio?
¿Cuál es el estado de elementos de salud del municipio?
¿Cuál es el estado de seguridad social del municipio?
¿Cuál es el estado de desigualdad del municipio?
¿Cuál es el estado de dependencia económica del municipio?
¿Cuál es el estado de calidad de vivienda del municipio?
¿Cuál es el estado de seguridad alimentaria del municipio?
```

**Ejemplo de respuesta:**
```
Alto
```

---

### 3. Prioridad de un Indicador

Consulta el nivel de prioridad de apoyo para un indicador específico. La prioridad es inversa al nivel de carencia (alta carencia = baja prioridad de apoyo recibido).

**Formato:**
```
¿Qué prioridad tiene [INDICADOR] del municipio?
```

**Ejemplos de preguntas:**
```
¿Qué prioridad tiene marginación del municipio?
¿Qué prioridad tiene educación del municipio?
¿Qué prioridad tiene servicios básicos del municipio?
¿Qué prioridad tiene conectividad del municipio?
¿Qué prioridad tiene rezago social del municipio?
¿Qué prioridad tiene elementos de salud del municipio?
¿Qué prioridad tiene seguridad social del municipio?
¿Qué prioridad tiene desigualdad del municipio?
¿Qué prioridad tiene dependencia económica del municipio?
¿Qué prioridad tiene calidad de vivienda del municipio?
¿Qué prioridad tiene seguridad alimentaria del municipio?
```

**Ejemplo de respuesta:**
```
Baja
```

---

### 4. Aspectos por Nivel de Carencia

Lista todos los indicadores que tienen un nivel de carencia específico.

**Formato:**
```
¿Cuáles aspectos del municipio tienen nivel [NIVEL]?
```

**Niveles disponibles:**
- `muy alto`
- `alto`
- `medio`
- `bajo`
- `muy bajo`

**Ejemplos de preguntas:**
```
¿Cuáles aspectos del municipio tienen nivel muy alto?
¿Cuáles aspectos del municipio tienen nivel alto?
¿Cuáles aspectos del municipio tienen nivel medio?
¿Cuáles aspectos del municipio tienen nivel bajo?
¿Cuáles aspectos del municipio tienen nivel muy bajo?
```

**Ejemplo de respuesta:**
```
Los siguientes aspectos del municipio Abejones tienen nivel de carencia "Alto":
• Marginación
• Elementos de Salud
• Seguridad Social
• Educación
• Dependencia Económica
```

---

### 5. Aspectos por Nivel de Prioridad

Lista todos los indicadores que requieren un nivel específico de prioridad de apoyo.

**Formato:**
```
¿Qué aspectos del municipio requieren prioridad [NIVEL]?
```

**Niveles de prioridad:**
- `muy alta`
- `alta`
- `media`
- `baja`
- `muy baja`

**Ejemplos de preguntas:**
```
¿Qué aspectos del municipio requieren prioridad muy alta?
¿Qué aspectos del municipio requieren prioridad alta?
¿Qué aspectos del municipio requieren prioridad media?
¿Qué aspectos del municipio requieren prioridad baja?
¿Qué aspectos del municipio requieren prioridad muy baja?
```

**Ejemplo de respuesta:**
```
Los siguientes aspectos del municipio Abejones que requieren una prioridad de apoyo "Alta":
• Conectividad
• Servicios Básicos
• Seguridad Alimentaria
```

---

## 🎯 Variaciones Permitidas

El sistema es flexible y acepta diferentes formas de hacer la misma pregunta:

### Para nombres de indicadores:
- ✅ Con acentos: `educación`, `marginación`
- ✅ Sin acentos: `educacion`, `marginacion`
- ✅ Con espacios: `servicios básicos`, `rezago social`
- ✅ Sin espacios: `serviciosbasicos`, `rezagosocial`

### Para niveles:
- ✅ Con espacios: `muy alto`, `muy bajo`
- ✅ Se normalizan automáticamente a: `muyalto`, `muybajo`

---

## 📝 Plantillas de Preguntas

### Estado General
```
¿Cuál es el estado del municipio?
```

### Estado de Indicador
```
¿Cuál es el estado de [INDICADOR] del municipio?
```
Donde `[INDICADOR]` puede ser:
- marginación / marginacion
- rezago social
- conectividad
- servicios básicos / servicios basicos
- elementos de salud
- seguridad social
- educación / educacion
- desigualdad
- dependencia económica / dependencia economica
- calidad de vivienda
- seguridad alimentaria

### Prioridad de Indicador
```
¿Qué prioridad tiene [INDICADOR] del municipio?
```

### Aspectos por Nivel de Carencia
```
¿Cuáles aspectos del municipio tienen nivel [NIVEL]?
```
Donde `[NIVEL]` puede ser:
- muy alto
- alto
- medio
- bajo
- muy bajo

### Aspectos por Prioridad
```
¿Qué aspectos del municipio requieren prioridad [NIVEL]?
```
Donde `[NIVEL]` puede ser:
- muy alta
- alta
- media
- baja
- muy baja

---

## 🔢 Matriz Completa de Preguntas Posibles

### Preguntas de Estado (11 indicadores)
1. ¿Cuál es el estado de marginación del municipio?
2. ¿Cuál es el estado de rezago social del municipio?
3. ¿Cuál es el estado de conectividad del municipio?
4. ¿Cuál es el estado de servicios básicos del municipio?
5. ¿Cuál es el estado de elementos de salud del municipio?
6. ¿Cuál es el estado de seguridad social del municipio?
7. ¿Cuál es el estado de educación del municipio?
8. ¿Cuál es el estado de desigualdad del municipio?
9. ¿Cuál es el estado de dependencia económica del municipio?
10. ¿Cuál es el estado de calidad de vivienda del municipio?
11. ¿Cuál es el estado de seguridad alimentaria del municipio?

### Preguntas de Prioridad (11 indicadores)
1. ¿Qué prioridad tiene marginación del municipio?
2. ¿Qué prioridad tiene rezago social del municipio?
3. ¿Qué prioridad tiene conectividad del municipio?
4. ¿Qué prioridad tiene servicios básicos del municipio?
5. ¿Qué prioridad tiene elementos de salud del municipio?
6. ¿Qué prioridad tiene seguridad social del municipio?
7. ¿Qué prioridad tiene educación del municipio?
8. ¿Qué prioridad tiene desigualdad del municipio?
9. ¿Qué prioridad tiene dependencia económica del municipio?
10. ¿Qué prioridad tiene calidad de vivienda del municipio?
11. ¿Qué prioridad tiene seguridad alimentaria del municipio?

### Preguntas por Nivel de Carencia (5 niveles)
1. ¿Cuáles aspectos del municipio tienen nivel muy alto?
2. ¿Cuáles aspectos del municipio tienen nivel alto?
3. ¿Cuáles aspectos del municipio tienen nivel medio?
4. ¿Cuáles aspectos del municipio tienen nivel bajo?
5. ¿Cuáles aspectos del municipio tienen nivel muy bajo?

### Preguntas por Prioridad (5 niveles)
1. ¿Qué aspectos del municipio requieren prioridad muy alta?
2. ¿Qué aspectos del municipio requieren prioridad alta?
3. ¿Qué aspectos del municipio requieren prioridad media?
4. ¿Qué aspectos del municipio requieren prioridad baja?
5. ¿Qué aspectos del municipio requieren prioridad muy baja?

### Pregunta General
1. ¿Cuál es el estado del municipio?

**Total: 33 tipos de preguntas básicas** (más todas sus variaciones)

---

## 💡 Consejos de Uso

1. **Selecciona primero un municipio**: Todas las consultas requieren que hayas seleccionado un municipio de la lista.

2. **Usa "del municipio"**: Agrega siempre "del municipio" al final de tus preguntas para mejores resultados.

3. **No te preocupes por acentos**: El sistema acepta tanto "educación" como "educacion".

4. **Los espacios son opcionales**: Puedes escribir "servicios básicos" o "serviciosbasicos".

5. **Experimenta**: El sistema es flexible con la sintaxis, prueba diferentes formas de preguntar.

---

## 🎨 Leyenda de Emojis en Respuestas

Cuando consultas el estado general, verás estos emojis según el nivel de carencia:

- 🔴 **Muy alto**: Nivel crítico de carencia
- 🟠 **Alto**: Nivel alto de carencia
- 🟡 **Medio**: Nivel medio de carencia
- 🟢 **Bajo**: Nivel bajo de carencia
- 🔵 **Muy bajo**: Nivel muy bajo de carencia

---

## ⚠️ Notas Importantes

### Relación Carencia-Prioridad

La relación entre carencia y prioridad es **inversa**:
- **Carencia Muy Alta** = Prioridad de Apoyo **Muy Baja**
- **Carencia Alta** = Prioridad de Apoyo **Baja**
- **Carencia Media** = Prioridad de Apoyo **Media**
- **Carencia Baja** = Prioridad de Apoyo **Alta**
- **Carencia Muy Baja** = Prioridad de Apoyo **Muy Alta**

### Formato de Respuestas

- Las respuestas simples (estado o prioridad) devuelven solo el nivel
- Las respuestas de lista muestran todos los aspectos que cumplen el criterio
- Si no hay aspectos que cumplan, recibirás un mensaje indicándolo

---

## 🚀 Ejemplos de Flujo Completo

### Ejemplo 1: Exploración Básica
```
1. Seleccionar: Abejones
2. Preguntar: ¿Cuál es el estado del municipio?
3. Ver: Tabla completa con todos los indicadores
4. Identificar: Educación está en nivel Alto
5. Preguntar: ¿Qué prioridad tiene educación del municipio?
6. Ver: Baja (porque alta carencia = baja prioridad)
```

### Ejemplo 2: Análisis por Nivel
```
1. Seleccionar: Oaxaca de Juárez
2. Preguntar: ¿Cuáles aspectos del municipio tienen nivel muy alto?
3. Ver: Lista de aspectos críticos
4. Preguntar: ¿Qué aspectos del municipio requieren prioridad muy alta?
5. Ver: Lista de aspectos que están bien y no requieren apoyo urgente
```

### Ejemplo 3: Análisis de Indicador Específico
```
1. Seleccionar: Santa María del Tule
2. Preguntar: ¿Cuál es el estado de servicios básicos del municipio?
3. Ver: Alto
4. Preguntar: ¿Qué prioridad tiene servicios básicos del municipio?
5. Ver: Baja
6. Conclusión: Hay alta carencia en servicios básicos
```

