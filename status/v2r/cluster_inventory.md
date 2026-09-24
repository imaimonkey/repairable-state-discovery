# V2R cluster inventory

2026-09-24T00:13:27.053052+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp', '/mnt/raid5'] | reference_compatible=False |

server1 `/`: 325570420736 available bytes; 81.84% used; 112500769 free inodes.

server1 `/home`: 325570420736 available bytes; 81.84% used; 112500769 free inodes.

server1 `/tmp`: 325570420736 available bytes; 81.84% used; 112500769 free inodes.

server1 `/var/tmp`: 325570420736 available bytes; 81.84% used; 112500769 free inodes.

server1 `/mnt/raid5`: 1211124056064 available bytes; 94.44% used; 337735341 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 41007628288 available bytes; 97.71% used; 110432400 free inodes.

server2 `/home`: 41007628288 available bytes; 97.71% used; 110432400 free inodes.

server2 `/tmp`: 41007628288 available bytes; 97.71% used; 110432400 free inodes.

server2 `/var/tmp`: 41007628288 available bytes; 97.71% used; 110432400 free inodes.

server2 `/mnt/raid5`: 533310447616 available bytes; 96.31% used; 445204204 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292602544128 available bytes; 83.67% used; 114209158 free inodes.

server3 `/home`: 292602544128 available bytes; 83.67% used; 114209158 free inodes.

server3 `/data`: 82254151680 available bytes; 98.86% used; 225844525 free inodes.

server3 `/tmp`: 292602544128 available bytes; 83.67% used; 114209158 free inodes.

server3 `/var/tmp`: 292602544128 available bytes; 83.67% used; 114209158 free inodes.
| server4 | True | ['3', '4', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106109149184 available bytes; 94.08% used; 114350807 free inodes.

server4 `/home`: 106109149184 available bytes; 94.08% used; 114350807 free inodes.

server4 `/data`: 292910563328 available bytes; 95.95% used; 225414568 free inodes.

server4 `/tmp`: 106109149184 available bytes; 94.08% used; 114350807 free inodes.

server4 `/var/tmp`: 106109149184 available bytes; 94.08% used; 114350807 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
