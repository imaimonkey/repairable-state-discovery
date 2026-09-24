# V2R cluster inventory

2026-09-24T02:26:46.364177+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 325388869632 available bytes; 81.85% used; 112498913 free inodes.

server1 `/home`: 325388869632 available bytes; 81.85% used; 112498913 free inodes.

server1 `/tmp`: 325388869632 available bytes; 81.85% used; 112498913 free inodes.

server1 `/var/tmp`: 325388869632 available bytes; 81.85% used; 112498913 free inodes.

server1 `/mnt/raid5`: 661591904256 available bytes; 96.97% used; 337733251 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 40892346368 available bytes; 97.72% used; 110431562 free inodes.

server2 `/home`: 40892346368 available bytes; 97.72% used; 110431562 free inodes.

server2 `/tmp`: 40892346368 available bytes; 97.72% used; 110431562 free inodes.

server2 `/var/tmp`: 40892346368 available bytes; 97.72% used; 110431562 free inodes.

server2 `/mnt/raid5`: 529124360192 available bytes; 96.34% used; 445199748 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 291857653760 available bytes; 83.71% used; 114163142 free inodes.

server3 `/home`: 291857653760 available bytes; 83.71% used; 114163142 free inodes.

server3 `/data`: 39720452096 available bytes; 99.45% used; 225845174 free inodes.

server3 `/tmp`: 291857653760 available bytes; 83.71% used; 114163142 free inodes.

server3 `/var/tmp`: 291857653760 available bytes; 83.71% used; 114163142 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106012311552 available bytes; 94.08% used; 114349853 free inodes.

server4 `/home`: 106012311552 available bytes; 94.08% used; 114349853 free inodes.

server4 `/data`: 289736314880 available bytes; 96.00% used; 225387568 free inodes.

server4 `/tmp`: 106012311552 available bytes; 94.08% used; 114349853 free inodes.

server4 `/var/tmp`: 106012311552 available bytes; 94.08% used; 114349853 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
