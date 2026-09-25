# V2R cluster inventory

2026-09-25T07:49:59.276714+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318861946880 available bytes; 82.21% used; 112480371 free inodes.

server1 `/home`: 318861946880 available bytes; 82.21% used; 112480371 free inodes.

server1 `/tmp`: 318861946880 available bytes; 82.21% used; 112480371 free inodes.

server1 `/var/tmp`: 318861946880 available bytes; 82.21% used; 112480371 free inodes.

server1 `/mnt/raid5`: 397386379264 available bytes; 98.18% used; 337558173 free inodes.
| server2 | True | ['0'] | [] | reference_compatible=False |

server2 `/`: 22848901120 available bytes; 98.73% used; 110410481 free inodes.

server2 `/home`: 22848901120 available bytes; 98.73% used; 110410481 free inodes.

server2 `/tmp`: 22848901120 available bytes; 98.73% used; 110410481 free inodes.

server2 `/var/tmp`: 22848901120 available bytes; 98.73% used; 110410481 free inodes.

server2 `/mnt/raid5`: 334526214144 available bytes; 97.69% used; 445095838 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84438511616 available bytes; 95.29% used; 114156051 free inodes.

server3 `/home`: 84438511616 available bytes; 95.29% used; 114156051 free inodes.

server3 `/data`: 142390714368 available bytes; 98.03% used; 225812384 free inodes.

server3 `/tmp`: 84438511616 available bytes; 95.29% used; 114156051 free inodes.

server3 `/var/tmp`: 84438511616 available bytes; 95.29% used; 114156051 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105637269504 available bytes; 94.11% used; 114350351 free inodes.

server4 `/home`: 105637269504 available bytes; 94.11% used; 114350351 free inodes.

server4 `/data`: 249046253568 available bytes; 96.56% used; 225011346 free inodes.

server4 `/tmp`: 105637269504 available bytes; 94.11% used; 114350351 free inodes.

server4 `/var/tmp`: 105637269504 available bytes; 94.11% used; 114350351 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
