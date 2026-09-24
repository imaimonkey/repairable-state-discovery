# V2R cluster inventory

2026-09-24T11:26:04.539417+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 324351508480 available bytes; 81.91% used; 112488865 free inodes.

server1 `/home`: 324351508480 available bytes; 81.91% used; 112488865 free inodes.

server1 `/tmp`: 324351508480 available bytes; 81.91% used; 112488865 free inodes.

server1 `/var/tmp`: 324351508480 available bytes; 81.91% used; 112488865 free inodes.

server1 `/mnt/raid5`: 453408382976 available bytes; 97.92% used; 337690033 free inodes.
| server2 | True | ['6'] | [] |

server2 `/`: 57669840896 available bytes; 96.78% used; 110430042 free inodes.

server2 `/home`: 57669840896 available bytes; 96.78% used; 110430042 free inodes.

server2 `/tmp`: 57669840896 available bytes; 96.78% used; 110430042 free inodes.

server2 `/var/tmp`: 57669840896 available bytes; 96.78% used; 110430042 free inodes.

server2 `/mnt/raid5`: 510773993472 available bytes; 96.47% used; 445173731 free inodes.
| server3 | True | [] | [] |

server3 `/`: 85749108736 available bytes; 95.21% used; 114197072 free inodes.

server3 `/home`: 85749108736 available bytes; 95.21% used; 114197072 free inodes.

server3 `/data`: 163839324160 available bytes; 97.74% used; 225816728 free inodes.

server3 `/tmp`: 85749108736 available bytes; 95.21% used; 114197072 free inodes.

server3 `/var/tmp`: 85749108736 available bytes; 95.21% used; 114197072 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105731051520 available bytes; 94.10% used; 114348877 free inodes.

server4 `/home`: 105731051520 available bytes; 94.10% used; 114348877 free inodes.

server4 `/data`: 115638595584 available bytes; 98.40% used; 225258071 free inodes.

server4 `/tmp`: 105731051520 available bytes; 94.10% used; 114348877 free inodes.

server4 `/var/tmp`: 105731051520 available bytes; 94.10% used; 114348877 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
