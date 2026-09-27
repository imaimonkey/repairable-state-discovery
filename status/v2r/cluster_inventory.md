# V2R cluster inventory

2026-09-27T03:45:37.981405+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 315076472832 available bytes; 82.42% used; 112443037 free inodes.

server1 `/home`: 315076472832 available bytes; 82.42% used; 112443037 free inodes.

server1 `/tmp`: 315076472832 available bytes; 82.42% used; 112443037 free inodes.

server1 `/var/tmp`: 315076472832 available bytes; 82.42% used; 112443037 free inodes.

server1 `/mnt/raid5`: 636783894528 available bytes; 97.08% used; 337401381 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 17626378240 available bytes; 99.02% used; 110365007 free inodes.

server2 `/home`: 17626378240 available bytes; 99.02% used; 110365007 free inodes.

server2 `/tmp`: 17626378240 available bytes; 99.02% used; 110365007 free inodes.

server2 `/var/tmp`: 17626378240 available bytes; 99.02% used; 110365007 free inodes.

server2 `/mnt/raid5`: 578221813760 available bytes; 96.00% used; 444882334 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 78696759296 available bytes; 95.61% used; 114062936 free inodes.

server3 `/home`: 78696759296 available bytes; 95.61% used; 114062936 free inodes.

server3 `/data`: 1335361908736 available bytes; 81.54% used; 225761315 free inodes.

server3 `/tmp`: 78696759296 available bytes; 95.61% used; 114062936 free inodes.

server3 `/var/tmp`: 78696759296 available bytes; 95.61% used; 114062936 free inodes.
| server4 | True | ['1', '3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111027769344 available bytes; 93.80% used; 114372977 free inodes.

server4 `/home`: 111027769344 available bytes; 93.80% used; 114372977 free inodes.

server4 `/data`: 383859933184 available bytes; 94.69% used; 224780827 free inodes.

server4 `/tmp`: 111027769344 available bytes; 93.80% used; 114372977 free inodes.

server4 `/var/tmp`: 111027769344 available bytes; 93.80% used; 114372977 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
