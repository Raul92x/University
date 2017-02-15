keytool -genkey                    \
        -alias dev                 \
        -keyalg RSA                \
        -keysize 2048              \
        -dname CN=localhost        \
        -keypass 123456            \
        -validity 10000            \
        -keystore cse405.keystore  \
        -storepass 123456
