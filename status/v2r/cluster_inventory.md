# V2R cluster inventory

2026-09-24T06:24:14.269682+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324509601792 available bytes; 81.90% used; 112491718 free inodes.

server1 `/home`: 324509601792 available bytes; 81.90% used; 112491718 free inodes.

server1 `/tmp`: 324509601792 available bytes; 81.90% used; 112491718 free inodes.

server1 `/var/tmp`: 324509601792 available bytes; 81.90% used; 112491718 free inodes.

server1 `/mnt/raid5`: 517575745536 available bytes; 97.63% used; 337723767 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 57883447296 available bytes; 96.77% used; 110431221 free inodes.

server2 `/home`: 57883447296 available bytes; 96.77% used; 110431221 free inodes.

server2 `/tmp`: 57883447296 available bytes; 96.77% used; 110431221 free inodes.

server2 `/var/tmp`: 57883447296 available bytes; 96.77% used; 110431221 free inodes.

server2 `/mnt/raid5`: 520432103424 available bytes; 96.40% used; 445192123 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 127198113792 available bytes; 92.90% used; 114196854 free inodes.

server3 `/home`: 127198113792 available bytes; 92.90% used; 114196854 free inodes.

server3 `/data`: 140557414400 available bytes; 98.06% used; 225835866 free inodes.

server3 `/tmp`: 127198113792 available bytes; 92.90% used; 114196854 free inodes.

server3 `/var/tmp`: 127198113792 available bytes; 92.90% used; 114196854 free inodes.
| server4 | True | ['1'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105805807616 available bytes; 94.10% used; 114349291 free inodes.

server4 `/home`: 105805807616 available bytes; 94.10% used; 114349291 free inodes.

server4 `/data`: 332643565568 available bytes; 95.40% used; 225373426 free inodes.

server4 `/tmp`: 105805807616 available bytes; 94.10% used; 114349291 free inodes.

server4 `/var/tmp`: 105805807616 available bytes; 94.10% used; 114349291 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
