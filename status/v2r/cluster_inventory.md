# V2R cluster inventory

2026-09-24T00:20:07.657687+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325556834304 available bytes; 81.84% used; 112500695 free inodes.

server1 `/home`: 325556834304 available bytes; 81.84% used; 112500695 free inodes.

server1 `/tmp`: 325556834304 available bytes; 81.84% used; 112500695 free inodes.

server1 `/var/tmp`: 325556834304 available bytes; 81.84% used; 112500695 free inodes.

server1 `/mnt/raid5`: 1183483691008 available bytes; 94.57% used; 337735234 free inodes.
| server2 | True | [] | [] |

server2 `/`: 41007128576 available bytes; 97.71% used; 110432376 free inodes.

server2 `/home`: 41007128576 available bytes; 97.71% used; 110432376 free inodes.

server2 `/tmp`: 41007128576 available bytes; 97.71% used; 110432376 free inodes.

server2 `/var/tmp`: 41007128576 available bytes; 97.71% used; 110432376 free inodes.

server2 `/mnt/raid5`: 533098905600 available bytes; 96.32% used; 445203672 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292638208000 available bytes; 83.67% used; 114209079 free inodes.

server3 `/home`: 292638208000 available bytes; 83.67% used; 114209079 free inodes.

server3 `/data`: 82247286784 available bytes; 98.86% used; 225844404 free inodes.

server3 `/tmp`: 292638208000 available bytes; 83.67% used; 114209079 free inodes.

server3 `/var/tmp`: 292638208000 available bytes; 83.67% used; 114209079 free inodes.
| server4 | True | ['1', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106096754688 available bytes; 94.08% used; 114350607 free inodes.

server4 `/home`: 106096754688 available bytes; 94.08% used; 114350607 free inodes.

server4 `/data`: 292913868800 available bytes; 95.95% used; 225414568 free inodes.

server4 `/tmp`: 106096754688 available bytes; 94.08% used; 114350607 free inodes.

server4 `/var/tmp`: 106096754688 available bytes; 94.08% used; 114350607 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
