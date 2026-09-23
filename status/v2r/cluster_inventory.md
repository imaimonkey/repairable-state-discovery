# V2R cluster inventory

2026-09-23T17:39:34.622558+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | False | [] | [] | reference_compatible=False |
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 41373810688 available bytes; 97.69% used; 110435438 free inodes.

server2 `/home`: 41373810688 available bytes; 97.69% used; 110435438 free inodes.

server2 `/tmp`: 41373810688 available bytes; 97.69% used; 110435438 free inodes.

server2 `/var/tmp`: 41373810688 available bytes; 97.69% used; 110435438 free inodes.

server2 `/mnt/raid5`: 546093543424 available bytes; 96.23% used; 445215612 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 294335320064 available bytes; 83.58% used; 114271700 free inodes.

server3 `/home`: 294335320064 available bytes; 83.58% used; 114271700 free inodes.

server3 `/data`: 53082820608 available bytes; 99.27% used; 225851856 free inodes.

server3 `/tmp`: 294335320064 available bytes; 83.58% used; 114271700 free inodes.

server3 `/var/tmp`: 294335320064 available bytes; 83.58% used; 114271700 free inodes.
| server4 | True | ['1', '2', '3', '5', '6'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111488684032 available bytes; 93.78% used; 114375784 free inodes.

server4 `/home`: 111488684032 available bytes; 93.78% used; 114375784 free inodes.

server4 `/data`: 7129174016 available bytes; 99.90% used; 225468891 free inodes.

server4 `/tmp`: 111488684032 available bytes; 93.78% used; 114375784 free inodes.

server4 `/var/tmp`: 111488684032 available bytes; 93.78% used; 114375784 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
