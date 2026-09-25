# V2R cluster inventory

2026-09-25T02:28:24.109975+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318969360384 available bytes; 82.21% used; 112480501 free inodes.

server1 `/home`: 318969360384 available bytes; 82.21% used; 112480501 free inodes.

server1 `/tmp`: 318969360384 available bytes; 82.21% used; 112480501 free inodes.

server1 `/var/tmp`: 318969360384 available bytes; 82.21% used; 112480501 free inodes.

server1 `/mnt/raid5`: 416220352512 available bytes; 98.09% used; 337606144 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 23016611840 available bytes; 98.72% used; 110410437 free inodes.

server2 `/home`: 23016611840 available bytes; 98.72% used; 110410437 free inodes.

server2 `/tmp`: 23016611840 available bytes; 98.72% used; 110410437 free inodes.

server2 `/var/tmp`: 23016611840 available bytes; 98.72% used; 110410437 free inodes.

server2 `/mnt/raid5`: 482930593792 available bytes; 96.66% used; 445113710 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84351655936 available bytes; 95.29% used; 114156073 free inodes.

server3 `/home`: 84351655936 available bytes; 95.29% used; 114156073 free inodes.

server3 `/data`: 145623699456 available bytes; 97.99% used; 225811084 free inodes.

server3 `/tmp`: 84351655936 available bytes; 95.29% used; 114156073 free inodes.

server3 `/var/tmp`: 84351655936 available bytes; 95.29% used; 114156073 free inodes.
| server4 | True | ['1', '5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105895915520 available bytes; 94.09% used; 114350978 free inodes.

server4 `/home`: 105895915520 available bytes; 94.09% used; 114350978 free inodes.

server4 `/data`: 24284958720 available bytes; 99.66% used; 224969421 free inodes.

server4 `/tmp`: 105895915520 available bytes; 94.09% used; 114350978 free inodes.

server4 `/var/tmp`: 105895915520 available bytes; 94.09% used; 114350978 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
