# V2R cluster inventory

2026-09-27T14:40:56.905686+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 304749920256 available bytes; 83.00% used; 112401381 free inodes.

server1 `/home`: 304749920256 available bytes; 83.00% used; 112401381 free inodes.

server1 `/tmp`: 304749920256 available bytes; 83.00% used; 112401381 free inodes.

server1 `/var/tmp`: 304749920256 available bytes; 83.00% used; 112401381 free inodes.

server1 `/mnt/raid5`: 630117953536 available bytes; 97.11% used; 337424044 free inodes.
| server2 | True | ['2'] | [] | reference_compatible=False |

server2 `/`: 13405732864 available bytes; 99.25% used; 110351797 free inodes.

server2 `/home`: 13405732864 available bytes; 99.25% used; 110351797 free inodes.

server2 `/tmp`: 13405732864 available bytes; 99.25% used; 110351797 free inodes.

server2 `/var/tmp`: 13405732864 available bytes; 99.25% used; 110351797 free inodes.

server2 `/mnt/raid5`: 525974765568 available bytes; 96.37% used; 444722192 free inodes.
| server3 | True | ['0', '1'] | [] | reference_compatible=True |

server3 `/`: 78558687232 available bytes; 95.62% used; 114062779 free inodes.

server3 `/home`: 78558687232 available bytes; 95.62% used; 114062779 free inodes.

server3 `/data`: 1328705978368 available bytes; 81.64% used; 225756678 free inodes.

server3 `/tmp`: 78558687232 available bytes; 95.62% used; 114062779 free inodes.

server3 `/var/tmp`: 78558687232 available bytes; 95.62% used; 114062779 free inodes.
| server4 | True | ['1', '3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 109770162176 available bytes; 93.87% used; 114372751 free inodes.

server4 `/home`: 109770162176 available bytes; 93.87% used; 114372751 free inodes.

server4 `/data`: 350472056832 available bytes; 95.16% used; 224727355 free inodes.

server4 `/tmp`: 109770162176 available bytes; 93.87% used; 114372751 free inodes.

server4 `/var/tmp`: 109770162176 available bytes; 93.87% used; 114372751 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
