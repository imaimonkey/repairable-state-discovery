# V2R cluster inventory

2026-09-24T03:27:59.936531+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 325355032576 available bytes; 81.85% used; 112498188 free inodes.

server1 `/home`: 325355032576 available bytes; 81.85% used; 112498188 free inodes.

server1 `/tmp`: 325355032576 available bytes; 81.85% used; 112498188 free inodes.

server1 `/var/tmp`: 325355032576 available bytes; 81.85% used; 112498188 free inodes.

server1 `/mnt/raid5`: 409210146816 available bytes; 98.12% used; 337733474 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 40841412608 available bytes; 97.72% used; 110431114 free inodes.

server2 `/home`: 40841412608 available bytes; 97.72% used; 110431114 free inodes.

server2 `/tmp`: 40841412608 available bytes; 97.72% used; 110431114 free inodes.

server2 `/var/tmp`: 40841412608 available bytes; 97.72% used; 110431114 free inodes.

server2 `/mnt/raid5`: 526766075904 available bytes; 96.36% used; 445198116 free inodes.
| server3 | True | ['1'] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292373303296 available bytes; 83.68% used; 114201080 free inodes.

server3 `/home`: 292373303296 available bytes; 83.68% used; 114201080 free inodes.

server3 `/data`: 36019032064 available bytes; 99.50% used; 225843060 free inodes.

server3 `/tmp`: 292373303296 available bytes; 83.68% used; 114201080 free inodes.

server3 `/var/tmp`: 292373303296 available bytes; 83.68% used; 114201080 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105987137536 available bytes; 94.09% used; 114349606 free inodes.

server4 `/home`: 105987137536 available bytes; 94.09% used; 114349606 free inodes.

server4 `/data`: 283975614464 available bytes; 96.08% used; 225385656 free inodes.

server4 `/tmp`: 105987137536 available bytes; 94.09% used; 114349606 free inodes.

server4 `/var/tmp`: 105987137536 available bytes; 94.09% used; 114349606 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
