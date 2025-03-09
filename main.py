# streamlit run main.py

import streamlit as st

from models import Me, Person, Transaction

st.title("Gue hutang siapa ???!")

if "me" not in st.session_state:
    st.session_state.me = Me()

page = st.sidebar.selectbox(
    "Menu",
    ["Hutang Gue", "Temen Gue"],
)


if page == "Temen Gue":
    st.write("### Tambah Temen")
    name = st.text_input("Nama")

    button = st.button("Tambah Temen")

    if button:
        new_member = Person(name)
        st.session_state.me.add_friend(new_member)
        st.rerun()

    st.write("### Teman Gue")
    if not st.session_state.me.friends:
        st.write("Belum punya temen, kasian gue :(")
    else:
        for friend in st.session_state.me.friends:
            st.write(friend.name)
            amount = int(
                st.number_input(
                    "Duit",
                    key=f"{friend.name}_amount",
                    value=0,
                    step=1000,
                )
            )
            lend = st.button("Gue minjemin", key=f"{friend.name}_lend")
            borrow = st.button("Gue hutang", key=f"{friend.name}_borrow")

            if lend:
                transaction = Transaction(amount)
                friend.transactions.append(transaction)
                st.rerun()

            if borrow:
                transaction = Transaction(amount)
                transaction.ask()
                friend.transactions.append(transaction)
                st.rerun()


elif page == "Hutang Gue":
    if not st.session_state.me.friends:
        st.write("Belum punya temen, kasian gue :(")

    else:
        friends = st.session_state.me.friends_has_debt()
        if not friends:
            st.write("Semua teman gue baik-baik aja, ga ada yang hutang sama gue :)")
        else:
            for friend in friends:
                st.write(friend.__str__())
