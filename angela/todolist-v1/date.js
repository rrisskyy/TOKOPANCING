exports.getDate = () => {
    const today = new Date();
    const option = {
        weekday: 'long',
        day: 'numeric',
        month: 'long' 
    };
    return today.toLocaleDateString('id-ID', option)
}


exports.getDay = () => {
    const today = new Date();
    const option = {
        weekday: 'long',
    };
    return today.toLocaleDateString('id-ID', option)
}

