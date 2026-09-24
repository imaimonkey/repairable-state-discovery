# V2R cluster inventory

2026-09-24T11:29:11.739255+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 324349022208 available bytes; 81.91% used; 112488855 free inodes.

server1 `/home`: 324349022208 available bytes; 81.91% used; 112488855 free inodes.

server1 `/tmp`: 324349022208 available bytes; 81.91% used; 112488855 free inodes.

server1 `/var/tmp`: 324349022208 available bytes; 81.91% used; 112488855 free inodes.

server1 `/mnt/raid5`: 427559198720 available bytes; 98.04% used; 337689622 free inodes.
| server2 | True | ['6', '7'] | [] |

server2 `/`: 57663877120 available bytes; 96.78% used; 110430007 free inodes.

server2 `/home`: 57663877120 available bytes; 96.78% used; 110430007 free inodes.

server2 `/tmp`: 57663877120 available bytes; 96.78% used; 110430007 free inodes.

server2 `/var/tmp`: 57663877120 available bytes; 96.78% used; 110430007 free inodes.

server2 `/mnt/raid5`: 510678339584 available bytes; 96.47% used; 445173615 free inodes.
| server3 | True | [] | [] |

server3 `/`: 85709258752 available bytes; 95.22% used; 114193583 free inodes.

server3 `/home`: 85709258752 available bytes; 95.22% used; 114193583 free inodes.

server3 `/data`: 163814121472 available bytes; 97.74% used; 225816669 free inodes.

server3 `/tmp`: 85709258752 available bytes; 95.22% used; 114193583 free inodes.

server3 `/var/tmp`: 85709258752 available bytes; 95.22% used; 114193583 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105730953216 available bytes; 94.10% used; 114348877 free inodes.

server4 `/home`: 105730953216 available bytes; 94.10% used; 114348877 free inodes.

server4 `/data`: 115636322304 available bytes; 98.40% used; 225258067 free inodes.

server4 `/tmp`: 105730953216 available bytes; 94.10% used; 114348877 free inodes.

server4 `/var/tmp`: 105730953216 available bytes; 94.10% used; 114348877 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
