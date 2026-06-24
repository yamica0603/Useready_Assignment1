import streamlit as st
import json
import tempfile
import pandas as pd

from src.document_processor import process_document


# ----------------------------------
# PAGE CONFIG
# ----------------------------------

st.set_page_config(
    page_title="Metadata Extractor",
    page_icon="📄",
    layout="wide"
)


# ----------------------------------
# HEADER
# ----------------------------------

st.markdown(
    """
    <h1 style='text-align: center; color: #1f77b4;'>
        Rental Agreement Metadata Extraction System
    </h1>

    <h4 style='text-align: center; color: gray;'>
        AI-Powered Metadata Extraction using PaddleOCR + Gemini
    </h4>

    <hr>
    """,
    unsafe_allow_html=True
)


# ----------------------------------
# SIDEBAR
# ----------------------------------

st.sidebar.title("About")

st.sidebar.info(
    """
    This application extracts metadata
    from rental agreements using:

    • PaddleOCR

    • Gemini 2.5 Flash

    • python-docx

    • Streamlit
    """
)

st.sidebar.markdown("---")

st.sidebar.write(
    "Supported Formats:"
)

st.sidebar.write(
    " DOCX"
)

st.sidebar.write(
    " PNG"
)

st.sidebar.write(
    " JPG"
)

st.sidebar.write(
    " JPEG"
)


# ----------------------------------
# UPLOAD SECTION
# ----------------------------------

st.markdown(
    """
    <h3 style='text-align: center;'>
        📄 Upload Rental Agreement
    </h3>
    """,
    unsafe_allow_html=True
)

uploaded_file = st.file_uploader(
    "",
    type=[
        "docx",
        "png",
        "jpg",
        "jpeg"
    ]
)


# ----------------------------------
# PROCESS FILE
# ----------------------------------

if uploaded_file is not None:

    st.success(
        f"Uploaded: {uploaded_file.name}"
    )

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=f"_{uploaded_file.name}"
    ) as tmp_file:

        tmp_file.write(
            uploaded_file.getbuffer()
        )

        temp_path = tmp_file.name

    with st.spinner(
        "Processing document..."
    ):

        try:

            result = process_document(
                temp_path
            )

            metadata = result[
                "metadata"
            ]

            text = result[
                "text"
            ]

            # ----------------------
            # METADATA DISPLAY
            # ----------------------

            st.markdown(
                """
                <h3 style='text-align: center; color: green;'>
                    ✅ Extracted Metadata
                </h3>
                """,
                unsafe_allow_html=True
            )

            col1, col2 = st.columns(2)

            with col1:

                st.metric(
                    "Agreement Value",
                    metadata.get(
                        "agreement_value",
                        ""
                    )
                )

                st.metric(
                    "Start Date",
                    metadata.get(
                        "agreement_start_date",
                        ""
                    )
                )

                st.metric(
                    "Party One",
                    metadata.get(
                        "party_one",
                        ""
                    )
                )

            with col2:

                st.metric(
                    "End Date",
                    metadata.get(
                        "agreement_end_date",
                        ""
                    )
                )

                st.metric(
                    "Notice Days",
                    metadata.get(
                        "renewal_notice_days",
                        ""
                    )
                )

                st.metric(
                    "Party Two",
                    metadata.get(
                        "party_two",
                        ""
                    )
                )

            st.markdown("---")

            # ----------------------
            # JSON OUTPUT
            # ----------------------

            st.subheader(
                "JSON Output"
            )

            st.json(
                metadata
            )

            # ----------------------
            # DOWNLOAD JSON
            # ----------------------

            json_data = json.dumps(
                metadata,
                indent=4
            )

            st.download_button(
                label="⬇ Download JSON",
                data=json_data,
                file_name="metadata.json",
                mime="application/json"
            )

            # ----------------------
            # DOWNLOAD CSV
            # ----------------------

            csv_df = pd.DataFrame(
                [metadata]
            )

            csv_data = csv_df.to_csv(
                index=False
            )

            st.download_button(
                label="⬇ Download CSV",
                data=csv_data,
                file_name="metadata.csv",
                mime="text/csv"
            )

            st.markdown("---")

            # ----------------------
            # EXTRACTED TEXT
            # ----------------------

            with st.expander(
                "View Extracted Text"
            ):

                st.text_area(
                    "Text",
                    text,
                    height=300
                )

        except Exception as e:

            st.error(
                f"Error: {str(e)}"
            )


# ----------------------------------
# FOOTER
# ----------------------------------

st.markdown("---")

st.markdown(
    """
    <div style='text-align: center; color: gray;'>
        Developed using Streamlit • PaddleOCR • Gemini 2.5 Flash
    </div>
    """,
    unsafe_allow_html=True
)