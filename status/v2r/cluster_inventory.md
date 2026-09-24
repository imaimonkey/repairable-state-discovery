# V2R cluster inventory

2026-09-24T15:29:21.600403+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324025040896 available bytes; 81.92% used; 112481433 free inodes.

server1 `/home`: 324025040896 available bytes; 81.92% used; 112481433 free inodes.

server1 `/tmp`: 324025040896 available bytes; 81.92% used; 112481433 free inodes.

server1 `/var/tmp`: 324025040896 available bytes; 81.92% used; 112481433 free inodes.

server1 `/mnt/raid5`: 416766586880 available bytes; 98.09% used; 337661269 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 57391898624 available bytes; 96.80% used; 110427511 free inodes.

server2 `/home`: 57391898624 available bytes; 96.80% used; 110427511 free inodes.

server2 `/tmp`: 57391898624 available bytes; 96.80% used; 110427511 free inodes.

server2 `/var/tmp`: 57391898624 available bytes; 96.80% used; 110427511 free inodes.

server2 `/mnt/raid5`: 502759153664 available bytes; 96.53% used; 445166140 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 84473315328 available bytes; 95.29% used; 114157052 free inodes.

server3 `/home`: 84473315328 available bytes; 95.29% used; 114157052 free inodes.

server3 `/data`: 160296652800 available bytes; 97.78% used; 225800124 free inodes.

server3 `/tmp`: 84473315328 available bytes; 95.29% used; 114157052 free inodes.

server3 `/var/tmp`: 84473315328 available bytes; 95.29% used; 114157052 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105716355072 available bytes; 94.10% used; 114348626 free inodes.

server4 `/home`: 105716355072 available bytes; 94.10% used; 114348626 free inodes.

server4 `/data`: 89399291904 available bytes; 98.76% used; 225256819 free inodes.

server4 `/tmp`: 105716355072 available bytes; 94.10% used; 114348626 free inodes.

server4 `/var/tmp`: 105716355072 available bytes; 94.10% used; 114348626 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
