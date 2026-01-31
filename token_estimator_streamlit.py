import streamlit as st


def estimate_tokens(text):
    return len(text) / 4


def count_words(text):
    return len(text.split())


def main():
    st.set_page_config(
        page_title="Token Estimator",
        page_icon="📝",
        layout="centered"
    )
    
    st.title("📝 Token Estimator")
    st.markdown("---")
    st.write("Upload a file to estimate the number of tokens.")
    st.info("**Assumption:** 1 token = 4 characters")
    
    uploaded_file = st.file_uploader(
        "Choose a file",
        type=['txt', 'md', 'py', 'json', 'csv', 'log'],
        help="Upload a text file to analyze"
    )
    
    if uploaded_file is not None:
        try:
            content = uploaded_file.read().decode('utf-8')
            
            char_count = len(content)
            word_count = count_words(content)
            token_estimate = estimate_tokens(content)
            
            st.markdown("---")
            st.subheader("📊 Analysis Results")
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric(
                    label="Characters",
                    value=f"{char_count:,}"
                )
            
            with col2:
                st.metric(
                    label="Words",
                    value=f"{word_count:,}"
                )
            
            with col3:
                st.metric(
                    label="Estimated Tokens",
                    value=f"{token_estimate:,.2f}"
                )
            
            if char_count > 4000:
                st.warning(
                    f"⚠️ **WARNING:** This file contains more than 4000 characters!\n\n"
                    f"Exceeds limit by **{char_count - 4000:,}** characters."
                )
            else:
                remaining = 4000 - char_count
                st.success(
                    f"✅ File is within the 4000 character limit.\n\n"
                    f"You have **{remaining:,}** characters remaining."
                )
            
            st.markdown("---")
            st.subheader("📄 File Preview")
            with st.expander("Click to view file content", expanded=False):
                st.text(content[:1000] + ("..." if len(content) > 1000 else ""))
                if len(content) > 1000:
                    st.caption(f"Showing first 1000 characters of {char_count:,} total")
            
        except UnicodeDecodeError:
            st.error("❌ Error: Unable to decode file. Please upload a text-based file.")
        except Exception as e:
            st.error(f"❌ Error reading file: {e}")
    
    st.markdown("---")
    st.caption("Token Estimator v1.0 | Built with Streamlit")


if __name__ == "__main__":
    main()
