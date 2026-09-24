# V2R cluster inventory

2026-09-24T15:26:16.485854+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324025806848 available bytes; 81.92% used; 112481442 free inodes.

server1 `/home`: 324025806848 available bytes; 81.92% used; 112481442 free inodes.

server1 `/tmp`: 324025806848 available bytes; 81.92% used; 112481442 free inodes.

server1 `/var/tmp`: 324025806848 available bytes; 81.92% used; 112481442 free inodes.

server1 `/mnt/raid5`: 416767856640 available bytes; 98.09% used; 337661621 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 57394528256 available bytes; 96.80% used; 110427541 free inodes.

server2 `/home`: 57394528256 available bytes; 96.80% used; 110427541 free inodes.

server2 `/tmp`: 57394528256 available bytes; 96.80% used; 110427541 free inodes.

server2 `/var/tmp`: 57394528256 available bytes; 96.80% used; 110427541 free inodes.

server2 `/mnt/raid5`: 502853840896 available bytes; 96.53% used; 445166262 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 84474277888 available bytes; 95.29% used; 114157048 free inodes.

server3 `/home`: 84474277888 available bytes; 95.29% used; 114157048 free inodes.

server3 `/data`: 160328142848 available bytes; 97.78% used; 225800194 free inodes.

server3 `/tmp`: 84474277888 available bytes; 95.29% used; 114157048 free inodes.

server3 `/var/tmp`: 84474277888 available bytes; 95.29% used; 114157048 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105716436992 available bytes; 94.10% used; 114348626 free inodes.

server4 `/home`: 105716436992 available bytes; 94.10% used; 114348626 free inodes.

server4 `/data`: 89404092416 available bytes; 98.76% used; 225256836 free inodes.

server4 `/tmp`: 105716436992 available bytes; 94.10% used; 114348626 free inodes.

server4 `/var/tmp`: 105716436992 available bytes; 94.10% used; 114348626 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
