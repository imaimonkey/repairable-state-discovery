# V2R cluster inventory

2026-09-25T02:49:52.880695+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318959824896 available bytes; 82.21% used; 112480443 free inodes.

server1 `/home`: 318959824896 available bytes; 82.21% used; 112480443 free inodes.

server1 `/tmp`: 318959824896 available bytes; 82.21% used; 112480443 free inodes.

server1 `/var/tmp`: 318959824896 available bytes; 82.21% used; 112480443 free inodes.

server1 `/mnt/raid5`: 416174170112 available bytes; 98.09% used; 337603633 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22999330816 available bytes; 98.72% used; 110410441 free inodes.

server2 `/home`: 22999330816 available bytes; 98.72% used; 110410441 free inodes.

server2 `/tmp`: 22999330816 available bytes; 98.72% used; 110410441 free inodes.

server2 `/var/tmp`: 22999330816 available bytes; 98.72% used; 110410441 free inodes.

server2 `/mnt/raid5`: 482514866176 available bytes; 96.67% used; 445113002 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84351369216 available bytes; 95.29% used; 114156077 free inodes.

server3 `/home`: 84351369216 available bytes; 95.29% used; 114156077 free inodes.

server3 `/data`: 145204813824 available bytes; 97.99% used; 225810855 free inodes.

server3 `/tmp`: 84351369216 available bytes; 95.29% used; 114156077 free inodes.

server3 `/var/tmp`: 84351369216 available bytes; 95.29% used; 114156077 free inodes.
| server4 | True | ['1', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 101767733248 available bytes; 94.32% used; 114350962 free inodes.

server4 `/home`: 101767733248 available bytes; 94.32% used; 114350962 free inodes.

server4 `/data`: 58924535808 available bytes; 99.19% used; 224968785 free inodes.

server4 `/tmp`: 101767733248 available bytes; 94.32% used; 114350962 free inodes.

server4 `/var/tmp`: 101767733248 available bytes; 94.32% used; 114350962 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
