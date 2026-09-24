# V2R cluster inventory

2026-09-24T00:24:15.935164+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp', '/mnt/raid5'] | reference_compatible=False |

server1 `/`: 325552930816 available bytes; 81.84% used; 112500653 free inodes.

server1 `/home`: 325552930816 available bytes; 81.84% used; 112500653 free inodes.

server1 `/tmp`: 325552930816 available bytes; 81.84% used; 112500653 free inodes.

server1 `/var/tmp`: 325552930816 available bytes; 81.84% used; 112500653 free inodes.

server1 `/mnt/raid5`: 1167650705408 available bytes; 94.64% used; 337735198 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 40998748160 available bytes; 97.71% used; 110432358 free inodes.

server2 `/home`: 40998748160 available bytes; 97.71% used; 110432358 free inodes.

server2 `/tmp`: 40998748160 available bytes; 97.71% used; 110432358 free inodes.

server2 `/var/tmp`: 40998748160 available bytes; 97.71% used; 110432358 free inodes.

server2 `/mnt/raid5`: 532967886848 available bytes; 96.32% used; 445203524 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292636700672 available bytes; 83.67% used; 114209079 free inodes.

server3 `/home`: 292636700672 available bytes; 83.67% used; 114209079 free inodes.

server3 `/data`: 82248425472 available bytes; 98.86% used; 225844333 free inodes.

server3 `/tmp`: 292636700672 available bytes; 83.67% used; 114209079 free inodes.

server3 `/var/tmp`: 292636700672 available bytes; 83.67% used; 114209079 free inodes.
| server4 | True | ['1', '3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106089738240 available bytes; 94.08% used; 114350499 free inodes.

server4 `/home`: 106089738240 available bytes; 94.08% used; 114350499 free inodes.

server4 `/data`: 292913774592 available bytes; 95.95% used; 225414569 free inodes.

server4 `/tmp`: 106089738240 available bytes; 94.08% used; 114350499 free inodes.

server4 `/var/tmp`: 106089738240 available bytes; 94.08% used; 114350499 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
