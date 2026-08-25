// ======================================
// Portal Notifications
// ======================================

let notificationModal = null;


// ======================================
// Criar modal
// ======================================

function createNotificationModal() {

    if (notificationModal) {

        return notificationModal;

    }

    notificationModal =
        document.createElement("div");

    notificationModal.id =
        "portal-notification-modal";

    notificationModal.className =
        "portal-notification-modal";

    notificationModal.innerHTML = `

        <div class="portal-notification-content">

            <div
                id="portal-notification-message"
                class="portal-notification-message"
            ></div>

            <div
                id="portal-notification-actions"
                class="portal-notification-actions"
            ></div>

        </div>

    `;

    document.body.appendChild(
        notificationModal
    );

    return notificationModal;

}


// ======================================
// Mostrar notificação
// ======================================

function showNotification(
    message,
    type
) {

    const modal =
        createNotificationModal();

    const messageElement =
        modal.querySelector(
            "#portal-notification-message"
        );

    const actions =
        modal.querySelector(
            "#portal-notification-actions"
        );

    messageElement.textContent =
        message;

    modal.className =
        `portal-notification-modal ${type}`;

    actions.innerHTML = `

        <button
            type="button"
            class="portal-notification-close"
            id="portal-notification-ok"
        >
            OK
        </button>

    `;

    const button =
        actions.querySelector(
            "#portal-notification-ok"
        );

    button.onclick = () => {

        closeNotification();

    };

    modal.hidden = false;

}


// ======================================
// Fechar notificação
// ======================================

function closeNotification() {

    if (!notificationModal) {

        return;

    }

    notificationModal.hidden = true;

}


// ======================================
// Sucesso
// ======================================

export function showSuccessNotification(
    message
) {

    showNotification(
        message,
        "success"
    );

}


// ======================================
// Erro
// ======================================

export function showErrorNotification(
    message
) {

    showNotification(
        message,
        "error"
    );

}


// ======================================
// Informação
// ======================================

export function showInfoNotification(
    message
) {

    showNotification(
        message,
        "info"
    );

}


// ======================================
// Aviso
// ======================================

export function showWarningNotification(
    message
) {

    showNotification(
        message,
        "warning"
    );

}


// ======================================
// Confirmação
// ======================================

export function showConfirmNotification(
    message
) {

    return new Promise(
        resolve => {

            const modal =
                createNotificationModal();

            const messageElement =
                modal.querySelector(
                    "#portal-notification-message"
                );

            const actions =
                modal.querySelector(
                    "#portal-notification-actions"
                );

            messageElement.textContent =
                message;

            modal.className =
                "portal-notification-modal warning";

            actions.innerHTML = `

                <button
                    type="button"
                    id="portal-notification-cancel"
                    class="portal-notification-cancel"
                >
                    Cancelar
                </button>

                <button
                    type="button"
                    id="portal-notification-confirm"
                    class="portal-notification-close"
                >
                    Confirmar
                </button>

            `;

            const cancelButton =
                actions.querySelector(
                    "#portal-notification-cancel"
                );

            const confirmButton =
                actions.querySelector(
                    "#portal-notification-confirm"
                );

            cancelButton.onclick = () => {

                closeNotification();

                resolve(false);

            };

            confirmButton.onclick = () => {

                closeNotification();

                resolve(true);

            };

            modal.hidden = false;

        }
    );

}