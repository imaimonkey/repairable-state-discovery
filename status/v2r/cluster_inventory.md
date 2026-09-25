# V2R cluster inventory

2026-09-25T07:31:37.159633+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318869364736 available bytes; 82.21% used; 112480370 free inodes.

server1 `/home`: 318869364736 available bytes; 82.21% used; 112480370 free inodes.

server1 `/tmp`: 318869364736 available bytes; 82.21% used; 112480370 free inodes.

server1 `/var/tmp`: 318869364736 available bytes; 82.21% used; 112480370 free inodes.

server1 `/mnt/raid5`: 385879597056 available bytes; 98.23% used; 337558395 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22860312576 available bytes; 98.72% used; 110410499 free inodes.

server2 `/home`: 22860312576 available bytes; 98.72% used; 110410499 free inodes.

server2 `/tmp`: 22860312576 available bytes; 98.72% used; 110410499 free inodes.

server2 `/var/tmp`: 22860312576 available bytes; 98.72% used; 110410499 free inodes.

server2 `/mnt/raid5`: 343164514304 available bytes; 97.63% used; 445097269 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84445196288 available bytes; 95.29% used; 114156035 free inodes.

server3 `/home`: 84445196288 available bytes; 95.29% used; 114156035 free inodes.

server3 `/data`: 142393163776 available bytes; 98.03% used; 225812682 free inodes.

server3 `/tmp`: 84445196288 available bytes; 95.29% used; 114156035 free inodes.

server3 `/var/tmp`: 84445196288 available bytes; 95.29% used; 114156035 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105637818368 available bytes; 94.11% used; 114350354 free inodes.

server4 `/home`: 105637818368 available bytes; 94.11% used; 114350354 free inodes.

server4 `/data`: 249092214784 available bytes; 96.56% used; 225014178 free inodes.

server4 `/tmp`: 105637818368 available bytes; 94.11% used; 114350354 free inodes.

server4 `/var/tmp`: 105637818368 available bytes; 94.11% used; 114350354 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
