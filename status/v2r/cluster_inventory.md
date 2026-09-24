# V2R cluster inventory

2026-09-24T04:07:19.059254+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324716691456 available bytes; 81.89% used; 112493464 free inodes.

server1 `/home`: 324716691456 available bytes; 81.89% used; 112493464 free inodes.

server1 `/tmp`: 324716691456 available bytes; 81.89% used; 112493464 free inodes.

server1 `/var/tmp`: 324716691456 available bytes; 81.89% used; 112493464 free inodes.

server1 `/mnt/raid5`: 421464956928 available bytes; 98.07% used; 337724765 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 40802123776 available bytes; 97.72% used; 110430818 free inodes.

server2 `/home`: 40802123776 available bytes; 97.72% used; 110430818 free inodes.

server2 `/tmp`: 40802123776 available bytes; 97.72% used; 110430818 free inodes.

server2 `/var/tmp`: 40802123776 available bytes; 97.72% used; 110430818 free inodes.

server2 `/mnt/raid5`: 526065483776 available bytes; 96.37% used; 445196653 free inodes.
| server3 | True | ['1'] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292027027456 available bytes; 83.70% used; 114176973 free inodes.

server3 `/home`: 292027027456 available bytes; 83.70% used; 114176973 free inodes.

server3 `/data`: 31742140416 available bytes; 99.56% used; 225841904 free inodes.

server3 `/tmp`: 292027027456 available bytes; 83.70% used; 114176973 free inodes.

server3 `/var/tmp`: 292027027456 available bytes; 83.70% used; 114176973 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105791000576 available bytes; 94.10% used; 114349483 free inodes.

server4 `/home`: 105791000576 available bytes; 94.10% used; 114349483 free inodes.

server4 `/data`: 256729907200 available bytes; 96.45% used; 225381880 free inodes.

server4 `/tmp`: 105791000576 available bytes; 94.10% used; 114349483 free inodes.

server4 `/var/tmp`: 105791000576 available bytes; 94.10% used; 114349483 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
