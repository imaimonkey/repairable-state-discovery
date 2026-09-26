# V2R cluster inventory

2026-09-26T08:42:49.649770+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318746861568 available bytes; 82.22% used; 112475802 free inodes.

server1 `/home`: 318746861568 available bytes; 82.22% used; 112475802 free inodes.

server1 `/tmp`: 318746861568 available bytes; 82.22% used; 112475802 free inodes.

server1 `/var/tmp`: 318746861568 available bytes; 82.22% used; 112475802 free inodes.

server1 `/mnt/raid5`: 219080298496 available bytes; 99.00% used; 337538889 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22313324544 available bytes; 98.76% used; 110403903 free inodes.

server2 `/home`: 22313324544 available bytes; 98.76% used; 110403903 free inodes.

server2 `/tmp`: 22313324544 available bytes; 98.76% used; 110403903 free inodes.

server2 `/var/tmp`: 22313324544 available bytes; 98.76% used; 110403903 free inodes.

server2 `/mnt/raid5`: 255330394112 available bytes; 98.24% used; 445024171 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 82678173696 available bytes; 95.39% used; 114110809 free inodes.

server3 `/home`: 82678173696 available bytes; 95.39% used; 114110809 free inodes.

server3 `/data`: 123903029248 available bytes; 98.29% used; 225828586 free inodes.

server3 `/tmp`: 82678173696 available bytes; 95.39% used; 114110809 free inodes.

server3 `/var/tmp`: 82678173696 available bytes; 95.39% used; 114110809 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106063732736 available bytes; 94.08% used; 114348137 free inodes.

server4 `/home`: 106063732736 available bytes; 94.08% used; 114348137 free inodes.

server4 `/data`: 89360502784 available bytes; 98.77% used; 224883411 free inodes.

server4 `/tmp`: 106063732736 available bytes; 94.08% used; 114348137 free inodes.

server4 `/var/tmp`: 106063732736 available bytes; 94.08% used; 114348137 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
