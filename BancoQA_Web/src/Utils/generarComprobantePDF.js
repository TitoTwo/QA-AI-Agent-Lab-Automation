import { jsPDF } from "jspdf";

import { formatoMoneda } from "./formatoMoneda";

export function generarComprobantePDF(tarjeta, operacion) {

    const pdf = new jsPDF();

    //=========================================
    // CONFIGURACIÓN GENERAL
    //=========================================

    let y = 20;

    pdf.setFont("helvetica", "bold");
    pdf.setFontSize(20);

    pdf.text("BANCO QA", 105, y, { align: "center" });

    y += 10;

    pdf.setFontSize(14);

    pdf.text(
        "COMPROBANTE DE FINANCIACIÓN",
        105,
        y,
        { align: "center" }
    );

    y += 8;

    pdf.line(20, y, 190, y);

    //=========================================
    // DATOS OPERACIÓN
    //=========================================

    y += 14;

    pdf.setFontSize(11);

    pdf.setFont("helvetica", "bold");

    pdf.text("Número de operación", 20, y);

    pdf.setFont("helvetica", "normal");

    pdf.text(
        operacion.numero_operacion,
        90,
        y
    );

    y += 8;

    pdf.setFont("helvetica", "bold");

    pdf.text("Fecha", 20, y);

    pdf.setFont("helvetica", "normal");

    pdf.text(
        operacion.fecha_operacion,
        90,
        y
    );

    y += 10;

    pdf.line(20, y, 190, y);

    //=========================================
    // TARJETA
    //=========================================

    y += 12;

    pdf.setFont("helvetica", "bold");

    pdf.text("Tarjeta", 20, y);

    y += 8;

    pdf.setFont("helvetica", "normal");

    pdf.text(
        tarjeta.nombre,
        20,
        y
    );

    y += 7;

    pdf.text(
        tarjeta.numero,
        20,
        y
    );

    y += 10;

    pdf.line(20, y, 190, y);

    //=========================================
    // DETALLE
    //=========================================

    y += 12;

    const agregarFila = (titulo, valor) => {

        pdf.setFont("helvetica", "bold");

        pdf.text(titulo, 20, y);

        pdf.setFont("helvetica", "normal");

        pdf.text(
            valor,
            90,
            y
        );

        y += 8;

    };

    agregarFila(
        "Monto financiado",
        formatoMoneda(operacion.monto, "ARS")
    );

    agregarFila(
        "Cantidad de cuotas",
        `${operacion.cuotas}`
    );

    agregarFila(
        "Valor por cuota",
        formatoMoneda(
            operacion.valor_cuota,
            "ARS"
        )
    );

    agregarFila(
        "TNA",
        `${operacion.tna}%`
    );

    agregarFila(
        "CFT",
        `${operacion.cft}%`
    );

    agregarFila(
        "Total estimado",
        formatoMoneda(
            operacion.total,
            "ARS"
        )
    );

    y += 6;

    pdf.line(20, y, 190, y);

    //=========================================
    // MENSAJE
    //=========================================

    y += 16;

    pdf.setFont("helvetica", "italic");

    pdf.setFontSize(10);

    pdf.text(
        "Gracias por operar con Banco QA.",
        105,
        y,
        {
            align: "center"
        }
    );

    y += 7;

    pdf.text(
        "Este comprobante corresponde a una simulación realizada desde BancoQA.",
        105,
        y,
        {
            align: "center"
        }
    );

    //=========================================
    // DESCARGA
    //=========================================

    pdf.save(
        `Comprobante_${operacion.numero_operacion}.pdf`
    );

}